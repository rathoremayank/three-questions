#!bin/bash

# Enabling Metadata
#aws ec2 modify-instance-metadata-options \
#    --instance-id i-02349991a3ca01eef \
#    --http-tokens required \
#    --http-endpoint enabled \
#    --instance-metadata-tags enabled

# Obtaining a Token 
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`

# To get available metadata items
#curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/

# To get tags from metadata 
#curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/tags/instance

