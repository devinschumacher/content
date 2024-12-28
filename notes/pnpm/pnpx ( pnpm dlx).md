`pnpx` is an alias for `pnpm dlx`

`pnpx` / `pnpm dlx` let's you use packages from the registry.npmjs.org package registry without installing them into your project as dependencies, or globally on your system. 

It "hot-loads" the package from the registry, runs whatever default command binary it exposes, and then cleans up afterwards.

---

## Why tho?

It's useful for one-time tasks or when you want to try out a tool without committing to installing it.

For example, maybe you...

1. Need to convert some files from format_a to format_b just once but dont need the whole package installed into your project permanently just to use it once and never use it again?

```
pnpm dlx json2csv -i input.json -o output.csv
```

2. Want to try out some tools, linters, or whatevers - and you aren't fully committed to perm-installing it into your project?

```
pnpm dlx eslint . 
pnpm dlx prettier --write .
```

## Comparisons

`pnpx` (`pnpm dlx`) is the "npm equivalent" to  `npx` - they both allow you to execute packages without installing them permanently.

They fetch the package, run it, and then clean up afterwards.