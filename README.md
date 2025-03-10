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

        Note: If error message is this: 
                Missing Requirements:
                    python==3.9.6
            Installation is not ok! [❌]
            
            Ignore it as this was added manually to requirements.txt

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


# Generating a Vocabulary Text File

16. java -jar jrdf2vec.jar -generateVocabularyFile walks/vectors.txt

# Analyzing the Embedding Vocabulary

17. java -jar ../../jar/jrdf2vec.jar -analyzeVocab sample_dbpedia_nt_file.nt /walks/model.kv

18. run flask app:
        flask --app python-server run
    run in debug mode: 
        flask --debug --app python_server run

# Tests:
    - command run from the following directory: /home/illusion/projects/docker/jRDF2Vec/jRDF2Vec-docker
    - test-1: java -jar ../../jar/jrdf2vec.jar -graph sample_dbpedia_nt_file.nt
    - test-2: java -Xmx10G -jar jar/jrdf2vec.jar -light test/test-2/orgs-iri-all.txt -graph test/test-2/orgs-full-graph-all.ttl
    - test-3: java -Xmx10G -jar jar/jrdf2vec.jar -trainingMode cbow -threads 24 -light test/test-2/orgs-iri-all.txt -graph test/test-2/orgs-full-graph-all.ttl
    - test-4: java -Xmx10G -jar jar/jrdf2vec.jar -trainingMode cbow -depth 10 -threads 30 -light test/test-2/orgs-iri-all.txt -graph test/test-2/orgs-full-graph-all.ttl

# Ollama:

- sudo systemctl stop ollama
- ollama serve

    NAME                    ID              SIZE    MODIFIED       
    codellama:13b           9f438cb9cd58    7.4 GB  33 seconds ago
    codellama:34b           685be00e1532    19 GB   5 minutes ago 
    codellama:70b           e59b580dfce7    38 GB   17 minutes ago
    codellama:7b            8fdf8f752f6e    3.8 GB  17 seconds ago
    codellama:latest        8fdf8f752f6e    3.8 GB  49 minutes ago
- 