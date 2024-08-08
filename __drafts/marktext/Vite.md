# Vite

![Screenshot 2023-12-02 at 03.10.44.png](/Users/devin/Library/Application%20Support/marktext/images/2609f495200958595de462dea84378fd098f82f1.png)

Vite is a JavaScript build tool. It bundles your JavaScript to improve performance on live sites by reducing the number of network requests. Vite uses [Rollup](https://rollupjs.org/) under the hood and is designed to handle the demands of JavaScript heavy projects.

---

## Rollup.js

![Screenshot 2023-12-02 at 03.10.21.png](/Users/devin/Library/Application%20Support/marktext/images/eaecc810c64f31597f620c1aa2649a9a6082f827.png)

### tree-shaking

Tree-shaking, also known as "live code inclusion", is Rollup's process of eliminating code that is not actually used in a given project. It is a [form of dead code elimination](https://medium.com/@Rich_Harris/tree-shaking-versus-dead-code-elimination-d3765df85c80#.jnypozs9n) but can be much more efficient than other approaches with regard to output size.

### Code Splitting[​](https://rollupjs.org/tutorial/#code-splitting)

For code splitting, there are cases where Rollup splits code into chunks automatically, like dynamic loading or multiple entry points, and there is a way to explicitly tell Rollup which modules to split into separate chunks via the [`output.manualChunks`](https://rollupjs.org/configuration-options/#output-manualchunks) option.
