FROM node:18 as build

WORKDIR /app
COPY react_app/package.json react_app/package-lock.json ./
RUN npm install
COPY react_app ./
RUN npm run build

FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/build /usr/share/nginx/html
