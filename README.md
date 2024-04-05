# jRDF2Vec






## steps to generate jar and save it locally and test locally
1. docker build -t jrdf2vec .
2. docker-compose -f docker-compose.yml up
3. docker exec -it jrdf2vec bash  [check the /app/jrdf2vec.jar if it exist]
    ## for window:
    ${PWD}
    - docker exec -it jrdf2vec sh -c "java -jar /app/jrdf2vec.jar -checkInstallation"
4. check installation status:
    java -jar /app/jrdf2vec.jar -checkInstallation [this is when inside the container]
    or
    docker exec -it jrdf2vec java -jar /app/jrdf2vec.jar -checkInstallation [this is to run when outside the container]
5. docker cp jrdf2vec:/app/jrdf2vec.jar ${PWD} [this will copy the jar available inside the container to the host machine]
6. java -jar ../../jar/jrdf2vec.jar -graph sample_dbpedia_nt_file.nt [test the jar]
7. java -jar ../../jar/jrdf2vec.jar -light sample_dbpedia_entity_file.txt -graph sample_dbpedia_nt_file.nt [test the jar]

## steps to generate jar and save it locally and test with docker

8. follow steps 1 & 2 as mentioned above.
9. docker exec -it jrdf2vec java -jar /app/jrdf2vec.jar -graph sample_dbpedia_nt_file.nt

docker run -it --rm \
  -v ${PWD}/data:/data \
  jrdf2vec-local \
  -light /data/src/test/resources/sample_dbpedia_entity_file.txt \
  -graph /data/src/test/resources/sample_dbpedia_nt_file.nt

  