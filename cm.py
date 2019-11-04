import numpy as np

def rewireERSIRsim(n, mu, Lambda, rho):

    pedge = mu/n
    njoin=np.zeros(n)
    link = np.zeros((10, max(n, np.ceil(mu + 5 * np.sqrt(mu)))))

    for i in range(1, n-1):
        for j in range(i+1, n):
            if np.random.rand < pedge:
                njoin[i] = njoin[i] + 1
                njoin[j] = njoin[j] + 1
                link[i,njoin[i]] = j
                link[j,njoin[j]] = i
    
    dmax = max(njoin)
    nedges = sum(njoin/2)

    state = np.zeros(n)

    # state(1) = 1
    state[0] = 1

    ninf = 1
    yinf = np.zeros(n)
    yinf[0] = 1

    infedges = np.zeros(nedges, 2)

    ninfe = 0

    for i in range(1, njoin[1]):
        j = link(1, i)
        if state[j] == 0
            ninfe = ninfe + 1
            infedges[ninfe, 1] = 1
            infedges[ninfe, 2] = j

    theta = Lambda / (Lambda + rho)
    LambdaPrho = Lambda + rho
    nm1 = n-1

    


    
def main():
    n = 1000
    mu = 1
    Lambda = 1
    rho = 0
    rewireERSIRsim(n, mu, Lambda, rho)

    print("The end")

if __name__ == "__main__":
    main()






