# ---- Dependencies ----
FROM node:20-alpine AS deps
WORKDIR /app

# Copy package.json + package-lock.json
COPY package*.json ./

# Copy tsconfig.json and next.config.js for path alias resolution
COPY tsconfig.json next.config.js ./

# Install all dependencies (including devDependencies needed for build)
RUN npm ci

# ---- Builder ----
FROM node:20-alpine AS builder
WORKDIR /app

# Copy node_modules from deps stage
COPY --from=deps /app/node_modules ./node_modules

# Copy all source code
COPY . .

# Disable Next.js telemetry
ENV NEXT_TELEMETRY_DISABLED 1

# Build Next.js app
RUN npm run build

# ---- Runner ----
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# Create user
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

# Copy only production-ready build files
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./ 
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000
ENV PORT=3000
ENV HOSTNAME=0.0.0.0

# Start the Next.js standalone server
CMD ["node", "server.js"]
