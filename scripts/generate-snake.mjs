import { mkdir, writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { getGithubUserContribution } from "@snk/github-user-contribution";
import { cellsToGrid } from "@snk/generate-snake-animation/cellsToGrid";
import { getBestRoute } from "@snk/solver/getBestRoute";
import { getPathToPose } from "@snk/solver/getPathToPose";
import { createSvg } from "@snk/svg-creator";
import { snake4 } from "@snk/types/__fixtures__/snake";

const DAY_MS = 24 * 60 * 60 * 1000;
const PERIOD_DAYS = 90;

// Retain real dates and weekdays, including the two partial boundary weeks.
export function selectRecentDays(cells, end) {
  const endTime = Date.parse(`${end}T00:00:00Z`);
  if (!Number.isFinite(endTime)) throw new Error("Invalid end date");
  const startTime = endTime - (PERIOD_DAYS - 1) * DAY_MS;
  const start = new Date(startTime).toISOString().slice(0, 10);
  const firstWeekday = new Date(startTime).getUTCDay();
  const recent = cells
    .filter((cell) => cell.date >= start && cell.date <= end)
    .sort((a, b) => a.date.localeCompare(b.date));

  if (recent.length !== PERIOD_DAYS) {
    throw new Error(`Expected ${PERIOD_DAYS} calendar days, received ${recent.length}`);
  }

  return recent.map((cell, index) => {
    const date = new Date(startTime + index * DAY_MS);
    if (
      cell.date !== date.toISOString().slice(0, 10) ||
      cell.y !== date.getUTCDay() ||
      !Number.isInteger(cell.count) || cell.count < 0 ||
      !Number.isInteger(cell.level) || cell.level < 0 || cell.level > 4
    ) {
      throw new Error(`Invalid or missing contribution data at ${cell.date}`);
    }
    return { ...cell, x: Math.floor((firstWeekday + index) / 7) };
  });
}

async function main() {
  const username = process.env.GITHUB_USERNAME;
  const githubToken = process.env.GITHUB_TOKEN;
  if (!username || !githubToken) throw new Error("GITHUB_USERNAME and GITHUB_TOKEN are required");

  // GitHub's default contribution calendar ends on the current UTC date.
  // Shanghai's next day is not available during 16:00–23:59 UTC.
  const end = new Date().toISOString().slice(0, 10);
  const cells = selectRecentDays(
    await getGithubUserContribution(username, { githubToken }), end,
  );
  const grid = cellsToGrid(cells);
  const chain = getBestRoute(grid, snake4);
  const returnPath = getPathToPose(chain.at(-1), snake4);
  if (!returnPath) throw new Error("Could not close the animation loop");
  chain.push(...returnPath);

  const svg = createSvg(grid, cells, chain, {
    colorEmpty: "#161d25",
    colorDots: { 1: "#0a4934", 2: "#0f8051", 3: "#2cba6d", 4: "#53e694" },
    colorDotBorder: "#1b1f230a",
    colorSnake: "#b48eff",
    sizeCell: 16,
    sizeDot: 12,
    sizeDotBorderRadius: 2,
  }, { stepDurationMs: 100 });
  const metadata = {
    username, start: cells[0].date, end, days: cells.length, weeks: grid.width,
    contributions: cells.reduce((sum, cell) => sum + cell.count, 0),
    activeDays: cells.filter((cell) => cell.count > 0).length,
  };
  await mkdir("dist", { recursive: true });
  await writeFile("dist/github-contribution-grid-snake-dark.svg", svg);
  await writeFile("dist/github-contribution-snake.json", `${JSON.stringify(metadata, null, 2)}\n`);
  console.log(JSON.stringify(metadata));
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main().catch((error) => {
    console.error(error.message);
    process.exitCode = 1;
  });
}
