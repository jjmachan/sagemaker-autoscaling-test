rm -rf OpenCVBlur*
python service.py
AWS_DEFAULT_OUTPUT=json
aws configure set default.region us-west-1
BENTO_BUNDLE_PATH=$(bentoml get OpenCVBlur:latest --print-location -q)
python aws-sagemaker-deploy/update.py $BENTO_BUNDLE_PATH bento-scale-test-2 sm.json