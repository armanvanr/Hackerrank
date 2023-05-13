def getMinCost(crew_id, job_id):
    crew_id = sorted(crew_id)
    job_id = sorted(job_id)
    sum_dist = 0
    for i in range(len(job_id)):
        dist=job_id[i] - crew_id[i]
        sum_dist+=abs(dist)
    return sum_dist

print(getMinCost([5,9,4,3,8,2], [9,8,1,10,1,4]))