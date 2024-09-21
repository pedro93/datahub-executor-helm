#! /bin/sh

export TAG=$1

updateVersion() {
    TAG=$1 yq -i e '.version |= env(TAG) ' $2;
    echo "Version is updated to $1 in $2"
}

# updating subcharts 
for file in charts/datahub-executor-worker/*/*/Chart.yaml; do 
   updateVersion $TAG $file
done

# updating datahub chart
updateVersion $TAG charts/datahub-executor-worker/Chart.yaml


 yq -i e ".dependencies[].version |= env(TAG)" charts/datahub-executor-worker/Chart.yaml