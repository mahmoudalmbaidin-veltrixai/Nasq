# Build context: repository root (see docker-compose.yml). Runs the Vite dev server.
FROM node:24.22.3-bookworm-slim

WORKDIR /app
RUN chown node:node /app
USER node

COPY --chown=node:node package.json package-lock.json .npmrc ./
COPY --chown=node:node apps/web/package.json apps/web/
RUN npm ci --workspace apps/web

COPY --chown=node:node apps/web apps/web

EXPOSE 5173
CMD ["npm", "run", "dev", "--workspace", "apps/web", "--", "--host", "0.0.0.0"]
