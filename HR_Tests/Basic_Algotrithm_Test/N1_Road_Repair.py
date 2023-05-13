def getMinCost(crew_id, job_id):
    crew_id = sorted(crew_id)
    job_id = sorted(job_id)
    sum_dist = 0
    for i in range(len(job_id)):
        dist=job_id[i] - crew_id[i]
        sum_dist+=abs(dist)
    return sum_dist

print(getMinCost([5,9,4,3,8,2], [9,8,1,10,1,4]))

# Problem Description
# A number of points along the highway are in need of repair.
# An equal number of crews are available, stationed at various points along the highway.
# They must move along the highway to reach an assigned point.
# Given that one crew must be assigned to each job,
# what is the minimum total amount of distance traveled by all crews before they can begin work?

# For example,
# given crews at points {1,3,5} and required repairs at {3,5,7},
# one possible minimum assignment would be
# {1→ 3, 3 → 5, 5 → 7} for a total of 6 units traveled.


# My algorithm:
# Since any crew can go to any point,
# sort the crew position ascending
# and do the same for the job's points.
# Calculate the absolute distance between crew and point for the same index respectfully,
# e.g. distance between crew[0] and job[0], crew[1] and job[1], ... use index-based loop obviously
# sum it all up