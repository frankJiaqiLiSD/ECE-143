import random

def multinomial_sample(n,p,k=1):  

    '''Generate samples from a multinomial distribution.'''

    assert n>0
    assert isinstance(n,int)
    assert k>0
    assert isinstance(k,int)
    for x in p:
        assert isinstance(x,(int,float))
        assert 0<=x<=1
    assert abs(sum(p) - 1) <= 1e-8

    total_probability = sum(p)
    p = [x / total_probability for x in p]
    cdf = []
    running = 0.0
    for prob in p:
        running += prob
        cdf.append(running)
    cdf[-1] = 1.0  

    samples = []
    for _ in range(k):
        counts = [0] * len(p)
        for _ in range(n):
            r = random.random()
            for i, cutoff in enumerate(cdf):
                if r <= cutoff:
                    counts[i] += 1
                    break

        samples.append(counts)

    return samples

if __name__ == "__main__":
    print(multinomial_sample(10,[1/3,1/3,1/3],k=10))