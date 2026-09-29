def passing_scores(scores):
    passed = []
    
    for index in range(len(scores)):

        if scores[index] >= 50:

            passed.append(scores[index])
            assert scores[index] >= 50, "score must be greater or equal to 50"

    assert 65 in scores, "Missing 65 in pass scores."

    return passed
    

print(passing_scores([49, 50, 80, 65]))