import numpy as np

def Max_Cut_Generator(N=100, d=1):
    Max_Cut = []
    for i in range(d):
        pool = np.linspace(1,N,N)
        for j in range(1,N+1):
            if j in pool:
                indices = np.where(pool==j)
                pool = np.delete(pool, indices)
                a = np.random.choice(pool)
                while [j,a,1] in Max_Cut:
                    print("repeat",[j,a,1])
                    a = np.random.choice(pool)
                Max_Cut.append([j,a,1])
                indices = np.where(pool==a)
                pool = np.delete(pool, indices)
    Max_Out = np.vstack(Max_Cut)
    return Max_Out

if __name__ in '__main__':
    demo = Max_Cut_Generator(N=16,d=4)
    print(demo)
