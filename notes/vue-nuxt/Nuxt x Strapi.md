## Reminders

  

Run the Project After Each Major Step: To identify issues early, run your project after each significant setup step, especially after adding or configuring new modules.

  

Check Compatibility: Always check the compatibility of major packages (like Apollo and GraphQL) with your project's version of Nuxt to avoid issues with peer dependencies.

  

```bash

pnpm outdated # This command will show you the current, wanted, and latest versions of your dependencies, which can help identify any potential compatibility issues.

```

  
  

## Installation & Setup Guide

  

### 1. Create the Project Folder

  

```bash

mkdir <project-name>

cd <project-name>

```

  
  

### 2. Create Strapi Project

  

```bash

nvm install 20.11.1

nvm use 20.11.1

pnpm create strapi-app backend --quickstart

```

  

2.1 Run the quickstart installation, or 'skip'

2.2 Register your admin user.

  
  

#### 3. Install GraphQL in Strapi

  

```bash

cd backend

rm yarn.lock

rm -rf node_modules

pnpm install

pnpx strapi install graphql # installs the Strapi GraphQL plugin, which adds GraphQL support to your Strapi project

pnpm install graphql # installs the graphql package itself, which is a dependency required by the GraphQL plugin to work correctly

```

  
  

### 4. Set Up Nuxt

  

```bash

cd ..

pnpm dlx nuxi@latest init frontend

cd frontend

touch server/schema.graphql

echo 'type Query { hello: String }' > server/schema.graphql

```

  
  

### 5. Add Apollo and GraphQL Server

  

```bash

pnpm add @apollo/client graphql @as-integrations/h3 nuxt-graphql-server @vue/apollo-composable

```

  
  

### 6. Configure Nuxt

  

```bash

mkdir -p plugins

touch plugins/apollo.client.ts

  

echo "import { ApolloClient, InMemoryCache } from '@apollo/client/core';" >> plugins/apollo.client.ts

echo "import { provideApolloClient } from '@vue/apollo-composable';" >> plugins/apollo.client.ts

echo "" >> plugins/apollo.client.ts

echo "export default defineNuxtPlugin((nuxtApp) => {" >> plugins/apollo.client.ts

echo " const apolloClient = new ApolloClient({" >> plugins/apollo.client.ts

echo " uri: 'http://localhost:1337/graphql', // Replace with your Strapi backend URL" >> plugins/apollo.client.ts

echo " cache: new InMemoryCache()," >> plugins/apollo.client.ts

echo " });" >> plugins/apollo.client.ts

echo "" >> plugins/apollo.client.ts

echo " provideApolloClient(apolloClient);" >> plugins/apollo.client.ts

echo " nuxtApp.vueApp.provide('apollo', apolloClient);" >> plugins/apollo.client.ts

echo "});" >> plugins/apollo.client.ts

```

  
  

### 7. Start the Projects

  

Start Strapi:

  

```bash

cd ../backend && pnpm develop

```

  

Start Nuxt:

```bash

cd frontend

rm -rf node_modules .nuxt

pnpm i && pnpm dev

```