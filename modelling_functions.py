# runs a filter on dta set to extract the months of actual growing season of crops
# months as numer ob month (jan=1, dec=12), cropyear as year of crop (relevant for crops 
# with growing seasons over calendar year)

def apply_growingseason(df, months, cropyear):
    start = months[0]-1
    stop  = months[-1]

    if months[0] > months[-1]:
        #empty filter
        filtr_clean = np.repeat(np.nan, 24).reshape(2, 12)

        #active filter
        filtr = filtr_clean
        filtr[0][start:] = 1
        filtr[1][:stop]  = 1
        
        dx = df.loc[(cropyear-1): cropyear].copy()
        dx = dx * filtr
        dx = dx.values.flatten().tolist()
        dx = np.array([x for x in dx if x > 0])      

    else:
        #empty filter
        filtr_clean = np.repeat(np.nan, 12)

        #active filter
        filtr = filtr_clean
        filtr[start:stop] = 1
        
        dx = df.loc[cropyear].copy()
        dx = dx * filtr
        dx = np.array(dx.dropna().tolist())
    
    return dx


# takes polynomial features and scaled polynomial features and fictional 
# preciperation to create fictional data row for modeling later
# typically used in a loop to create data sets for ranges from 0 to 1000mmm

def compute_fict(X_poly, X_scal, X_mean, X_sd, newRR):

    dx_p = X_poly
    dx_s = X_scal

    new_rr = float(newRR)

    # auswirkungen auf [3, 15, 8, 12, 16, 17]
    # [3]     x2 = RR
    # [8]  x0 x2 = TT*RR
    # [15]  x2^2 = RR^2
    # [12] x1 x2 = SD*RR
    # [16] x2 x3 = RR*OB
    # [17] x2 x4 = RR*GB

    # [3]     x2 = RR
    x2_n  = new_rr #absolut
    x2_s  = (x2_n - X_mean[0]) / X_sd[0] #scaled

    # [15]  x2^2 = RR^2
    x22_n = x2_n**2 #absolut
    x22_s = (x22_n - X_mean[1]) / X_sd[1] #scaled

    # [8]  x0 x2 = TT*RR
    x0x2_n = dx_p[1] * x2_n
    x0x2_s = (x0x2_n - X_mean[2]) / X_sd[2]

    # [12] x1 x2 = SD*RR
    x1x2_n = dx_p[2] * x2_n
    x1x2_s = (x1x2_n - X_mean[3]) / X_sd[3]

    # [16] x2 x3 = RR*OB
    x2x3_n = x2_n * dx_p[4]
    x2x3_s = (x2x3_n - X_mean[4]) / X_sd[4]

    # [17] x2 x4 = RR*GB
    x2x4_n = x2_n * dx_p[5]
    x2x4_s = (x2x4_n - X_mean[5]) / X_sd[5]

    dx_new = dx_s.copy()
    dx_new[3]  = x2_s
    dx_new[15] = x22_s
    dx_new[8] = x0x2_s
    dx_new[12] = x1x2_s
    dx_new[16] = x2x3_s
    dx_new[17] = x2x4_s

    return dx_new