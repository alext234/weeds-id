
Playground to experiment various machine learning models to class a plant picture as a weed or  not.


## Development

### Docker images


* For data processing 

```
docker run  -p 8888:8888 -it -v $PWD:/weeds -w /weeds alext234/datascience:latest  bash 
```

Start jupyter notebook 

```
jupyter notebook --allow-root --ip=0.0.0.0
```

* For tensorflow

```
alext234/tensorflow:latest-py3
```