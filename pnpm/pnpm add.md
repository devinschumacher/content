# pnpm add <pkg>

`# pnpm add <pkg>` Installs a package and any packages that it depends on (as a production dependency by default).

---

`pnpm add <pkg>` doesn't immediately [pnpm install](pnpm%20install.md) the package, it: 

1. adds the package to the `dependencies` object in your `package.json` file.
2. updates the `pnpm-lock.yaml` file (if it exists) to include information about the new package.

*However, it doesn't download or install the package files into your `node_modules` directory at this point.*

The actual installation (downloading and linking of packages) happens when you run [pnpm install](pnpm%20install.md) -- or when you run your project's scripts that trigger an install