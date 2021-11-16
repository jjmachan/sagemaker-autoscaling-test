# Sagemaker Autoscaling Test

## IrisClassifier

This is the first test model we have. Based on the age old sklearn
irisclassifier. This should work on CPUs and on cheap instances.

./irisclassifier-bento - contains the bento that we can use. You can also use
`classifier.py` and `training.py` to create bentos
./irisclassifier-deployable - the deployable for IrisClassifier that is made for
deploying into sagemaker.
./sagemaker_template.yaml - The Cloudformation template that will be used
deploy.
