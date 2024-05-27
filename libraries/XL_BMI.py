# -----------------------------------------------------------
#Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
#@author cafedevn
#Contact: cafedevn@gmail.com
#Fanpage: https://www.facebook.com/cafedevn
#Group: https://www.facebook.com/groups/cafedev.vn/
#Instagram: https://instagram.com/cafedevn
#Twitter: https://twitter.com/CafedeVn
#Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
#Pinterest: https://www.pinterest.com/cafedevvn/
#YouTube: https://www.youtube.com/channel/UCE7zpY_SlHGEgo67pHxqIoA/
# -----------------------------------------------------------


def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang / (chieu_cao * chieu_cao)
    return bmi

def ket_luan(bmi):
    kl = ''
    if bmi < 18.5:
        kl = 'Bạn gầy'
    elif bmi < 25:
        kl = 'Bạn bình thường'
    else:
        kl = 'Bạn thừa cân'
    return kl
