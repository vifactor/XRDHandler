import xrayutilities as xu

class RSMPeak:
    def __init__(self, name, pos_x, pos_y, sigma_x = 0.001, sigma_y = 0.001, angle = 0.0, scale = 1.0, background = 0.0):
        """initializes peak on a reciprocal space map"""
        #peak name
        self.name = name
        #peak position
        self.pos_x = pos_x
        self.pos_y = pos_y
        #peak width
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
        #peak rotation angle
        self.angle = angle
        #RSM scale and background values
        self.scale = scale
        self.background = background
        
        #covariance matrix obtained as a result of the fit
        self.covariance = None
    
    def Fit(self, x, y, z, fitrange):
        """Fits a peak on a RSM defined by (x, y, z)-data to 2d Gaussian"""
        #define ranges of data to which the peak will be fitted
        range_x, range_y = fitrange
        xmin = self.pos_x - range_x / 2
        xmax = self.pos_x + range_x / 2
        ymin = self.pos_y - range_y / 2
        ymax = self.pos_y + range_y / 2
        
        #xrayutilities fit function
        fitparams, self.covariance = xu.math.fit.fit_peak2d(x, y, z, 
                    [self.pos_x, self.pos_y, self.sigma_x, self.sigma_y, self.scale, self.background, self.angle], 
                    [xmin, xmax, ymin, ymax],
                    xu.math.functions.Gauss2d, 50000)
        
        self.pos_x = fitparams[0]
        self.pos_y = fitparams[1]
        
        self.sigma_x = fitparams[2]
        self.sigma_y = fitparams[3]
        
        self.scale = fitparams[4]
        self.background = fitparams[5]
        self.angle = fitparams[6]
        
        print "pos:", self.pos_x, self.pos_y
        print "sigma:", self.sigma_x, self.sigma_y
        print "sc, bg, ang", self.scale, self.background, self.angle
        
        print self.covariance
