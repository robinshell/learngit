import math
class GPSTrans():
    pi = 3.1415926535897932384626 
    x_pi = 3.14159265358979324 * 3000.0 / 180.0 
    a = 6378245.0 
    ee = 0.00669342162296594323  

    def transformLat(self,x,y):
        ret = -100.0+2 *x +3* y + 0.2 * y * y + 0.1 * x * y+0.2 * math.sqrt(abs(x))  
        ret += (20.0 * math.sin(6.0 * x * self.pi) + 20.0 * math.sin(2.0 * x * self.pi)) * 2/3 
        ret += (20.0 * math.sin(y * self.pi) + 40.0 * math.sin(y / 3.0 * self.pi)) * 2 /3 
        ret += (160.0 * math.sin(y/12.0*self.pi) + 320 * math.sin(y * self.pi / 30.0)) * 2/3 
        return ret 
 

    def transformLon(self, x, y):
        ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1  * math.sqrt(abs(x))  
        ret += (20.0 * math.sin(6.0 * x * self.pi) + 20.0 * math.sin(2.0 * x * self.pi)) * 2.0 / 3.0  
        ret += (20.0 * math.sin(x * self.pi) + 40.0 * math.sin(x / 3.0 * self.pi)) * 2.0 / 3.0  
        ret += (150.0 * math.sin(x / 12.0 * self.pi) + 300.0 * math.sin(x / 30.0  * self.pi)) * 2.0 / 3.0 
        return ret 
  
    def transform(self, lat, lon):
        if (self.outOfChina(lat, lon)): 
            return [lat,lon]  
  
        dLat = self.transformLat(lon - 105.0, lat - 35.0) 
        dLon = self.transformLon(lon - 105.0, lat - 35.0) 
        radLat = lat / 180.0 * self.pi  
        magic = math.sin(radLat) 
        magic = 1 - self.ee * magic * magic  
        sqrtMagic = math.sqrt(magic) 
        dLat = (dLat * 180.0) / ((self.a * (1 - self.ee)) / (magic * sqrtMagic) * self.pi)  
        dLon = (dLon * 180.0) / (self.a / sqrtMagic * math.cos(radLat) * self.pi)  
        mgLat = lat + dLat  
        mgLon = lon + dLon  
        return [mgLat,mgLon]  
 
    def outOfChina(self, lat, lon): 
        if lon < 72.004 or lon > 137.8347:  
            return True  
        if lat < 0.8293 or lat > 55.8271:  
            return True 
        return False  

    ''' 
     * 84 to 火星坐标系 (GCJ-02) World Geodetic System ==> Mars Geodetic System 
     * 
     * @param lat 
     * @param lon 
     * @return 
     ''' 
    def gps84_To_Gcj02(self, lat,lon): 
        if (self.outOfChina(lat, lon)):  
            return [lat,lon] 
     
        dLat = self.transformLat(lon - 105.0, lat - 35.0)  
        dLon = self.transformLon(lon - 105.0, lat - 35.0) 
        radLat = lat / 180.0 * self.pi  
        magic = math.sin(radLat)  
        magic = 1 - self.ee * magic * magic  
        sqrtMagic = math.sqrt(magic)  
        dLat = (dLat * 180.0) / ((self.a * (1 - self.ee)) / (magic * sqrtMagic) * self.pi)  
        dLon = (dLon * 180.0) / (self.a / sqrtMagic * math.cos(radLat) * self.pi)  
        mgLat = lat + dLat  
        mgLon = lon + dLon 
        return [self.retain6(mgLat), self.retain6(mgLon)] 


    '''/** 
     * * 火星坐标系 (GCJ-02) to 84 * * @param lon * @param lat * @return 
     * */'''  
    def gcj02_To_Gps84(self, lat, lon): 
        gps = self.transform(lat, lon)  
        lontitude = lon * 2 - gps[1]  
        latitude = lat * 2 - gps[0]  
        return [ round(lontitude,6),round(latitude,6)]  
  
    '''/** 
     * 火星坐标系 (GCJ-02) 与百度坐标系 (BD-09) 的转换算法 将 GCJ-02 坐标转换成 BD-09 坐标 
     * 
     * @param lat 
     * @param lon 
     */ ''' 
    def gcj02_To_Bd09(self,lat, lon):  
        x = lon
        y = lat 
        z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * self.x_pi)  
        theta = math.atan2(y, x) + 0.000003 * math.cos(x * self.x_pi)  
        tempLon = z * math.cos(theta) + 0.0065  
        tempLat = z * math.sin(theta) + 0.006 
        gps = [self.retain6(tempLat),self.retain6(tempLon)] 
        return gps  
  

    '''/** 
     * * 火星坐标系 (GCJ-02) 与百度坐标系 (BD-09) 的转换算法 * * 将 BD-09 坐标转换成GCJ-02 坐标 * * @param 
     * bd_lat * @param bd_lon * @return 
     */'''  
    def bd09_To_Gcj02(self, lat, lon):
        x = lon - 0.0065
        y = lat - 0.006 
        z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * self.x_pi)  
        theta = math.atan2(y, x) - 0.000003 * math.cos(x * self.x_pi)  
        tempLon = z * math.cos(theta)  
        tempLat = z * math.sin(theta)  
        gps = [tempLat,tempLon]  
        return gps  
  

    '''/**将gps84转为bd09 
     * @param lat 
     * @param lon 
     * @return 
     */ ''' 
    def gps84_To_bd09(self, lat, lon):  
        gcj02 = self.gps84_To_Gcj02(lat,lon) 
        bd09 = self.gcj02_To_Bd09(gcj02[0],gcj02[1])  
        return bd09  
  
    def bd09_To_gps84(self, lat,lon): 
        gcj02 = self.bd09_To_Gcj02(lat, lon)  
        gps84 = self.gcj02_To_Gps84(gcj02[0], gcj02[1])  
        #保留小数点后五位  
        gps84[0] = self.retain6(gps84[0])  
        gps84[1] = self.retain6(gps84[1])  
        return gps84  
 

    '''/**保留小数点后六位 
     * @param num 
     * @return 
     */'''  
    def retain6(self, num):    
        return round(num,6) 
  
a=GPSTrans()
s=[]
'''
points=[[120.367535,31.542001],[120.367935,31.542279],#1区12
        [120.368151,31.542425],[120.368493,31.542668],#2区12
        [120.367861,31.541664],[120.368261,31.541942],#1区43
        [120.368469,31.542094],[120.368807,31.542331],#2区43
        [120.368091,31.541434],[120.368479,31.541715],#3区12
        [120.368697,31.541861],[120.369037,31.542095],#4区12
        [120.368415,31.541098],[120.368799,31.541367],#3区43
        [120.369020,31.541521],[120.369347,31.541768],#4区43
        [120.368564,31.540941],[120.368942,31.541208],#5区12
        [120.369192,31.541319],[120.369536,31.541557],#6区12
        [120.368956,31.540517],[120.369351,31.540787],#5区43
        [120.369510,31.540983],[120.369850,31.541218]]#6区43
for point in points:
    s.append(a.gcj02_To_Gps84(point[1], point[0]))'''
s.append(a.gcj02_To_Gps84(31.541234, 120.369541))
print(s)
