FROM nginx:alpine

#copy frontend file to dir in nginx 
COPY index.html /usr/share/nginx/html/index.html
# change owner of the nginx dir
RUN chown nginx:nginx /usr/share/nginx/html/*
