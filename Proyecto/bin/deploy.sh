# terminate on any error
set -e

. .env

npm run build

# ********* RUN TESTS *********
docker build -f Dockerfile . -t backend
docker run -p 5501:5500 -d --name test_backend_run backend
# use a Postman environment switch tests over to run against container on http://localhost:5501
set +e
newman run https://api.getpostman.com/collections/1559645-9f5aa83b-666d-41ef-9b91-6c3ec25ef789?apikey=${POSTMAN} -e https://api.getpostman.com/environments/1559645-b5c093e1-bf72-4f7e-b18a-11263f21ec32?apikey=${POSTMAN} --ignore-redirects
EXIT_CODE=$?
docker stop test_backend_run
docker rm test_backend_run
# # if the previous tests failed, remember to shut down the local container
if [[ $EXIT_CODE != 0 ]]; then exit $EXIT_CODE; fi
set -e


# ********* DEPLOY TO PRODUCTION *********

# git revision
GIT_REV=$(git rev-parse --short HEAD)

# build docker container for front end, and tag container name
docker build -f Dockerfile.ui . -t ${Shynriuh}/cat-ui:${GIT_REV} -t ${Shynriuh}/cat-ui:prod
docker push ${Shynriuh}/cat-ui:${GIT_REV}

# deploy backend to kubernetes
# will look for a kube config, and if none exists prompt to set up via kubesail
npx deploy-to-kube --no-confirm

# deploy frontend and tell kubernetes to use newest UI image
kubectl apply -f deployment-ui-prod.yaml
kubectl set image deployment/cat-ui cat-ui=${Shynriuh}/cat-ui:${GIT_REV}
