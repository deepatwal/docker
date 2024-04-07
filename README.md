# jRDF2Vec

## steps to generate jar and save it locally and test locally
1. docker build --no-cache -t jrdf2vec . [/home/illusion/projects/docker/jRDF2Vec/jRDF2Vec-src]
2. docker-compose -f docker-compose.yml up [/home/illusion/projects/docker/jRDF2Vec/jRDF2Vec-docker]
3. docker exec -it jrdf2vec bash  [check the /app/jrdf2vec.jar if it exist]
    ## for window:
        - ${PWD}
        - docker exec -it jrdf2vec sh -c "java -jar /app/jrdf2vec.jar -checkInstallation"
4. check installation status:

    - activate the conda env jrdf2vec_3_9_env and use the correct requirements.txt [requirements-correct.txt]
        java -jar /app/jrdf2vec.jar -checkInstallation [this is when inside the container]
            or
        docker exec -it jrdf2vec java -jar /app/jrdf2vec.jar -checkInstallation [this is to run when outside the container]
5. docker cp jrdf2vec:/app/jrdf2vec.jar ${PWD} [this will copy the jar available inside the container to the host machine]
6. java -jar ../../jar/jrdf2vec.jar -graph sample_dbpedia_nt_file.nt [test the jar]
7. java -jar ../../jar/jrdf2vec.jar -light sample_dbpedia_entity_file.txt -graph sample_dbpedia_nt_file.nt [test the jar]

## steps to generate jar and save it locally and test with docker

8. follow steps 1 & 2 as mentioned above.
9. docker exec -it jrdf2vec java -jar /app/jrdf2vec.jar -graph sample_dbpedia_nt_file.nt

10. docker command:
docker run -it --rm \
-v ${PWD}/data:/data \
jrdf2vec-local \
-light /data/src/test/resources/sample_dbpedia_entity_file.txt \
-graph /data/src/test/resources/sample_dbpedia_nt_file.nt


# Run Jar to generate vectors:

12. cd /home/illusion/projects/docker/jRDF2Vec/jRDF2Vec-docker/test
13. create test folders: test1 and copy the relevant graph files
14. cd /test1 and run following: java -jar ../../jar/jrdf2vec.jar -graph sample_dbpedia_nt_file.nt
15. check if the model.kv and vectors.txt file generated successfully.


  