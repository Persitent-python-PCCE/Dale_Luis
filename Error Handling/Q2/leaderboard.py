top_reps = ["A. Chen","R. Patel", "M. Silva", "K. Osei"]
quota_hit = {"A. Chen": 112, "R. Patel": 98, "M. Silva": 87}

def rep_at_rank(rank):
    try:
        return top_reps[rank - 1]
    except IndexError:
        print(f"No rep at rank {rank}.")
        return None
    
    


def quota_for(rep):
    try:
        return quota_hit[rep]
    except KeyError:
        print(f"No quota record for {rep}.")
        return None

def safe_report(rank, rep):
    try:
        print(f"Rank {rank}: {top_reps[rank - 1]}")
        print(f"Quota: {quota_hit[rep]}%")
    except LookupError:
        print("Lookup failed.")
    pass


print(rep_at_rank(2))
print(rep_at_rank(10))
print(quota_for("M. Silva"))
print(quota_for("J. Doe"))

safe_report(2, "M. Silva")
safe_report(10, "J. Doe")