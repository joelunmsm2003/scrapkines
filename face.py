curl -X GET "https://graph.facebook.com/oauth/access_token?client_id=279190169884971&client_secret=f2868d593b4b54387d5b14c7b1651d36&grant_type=client_credentials" 

279190169884971|KDCzLdgTS80Sk5FwhQb7WGo3TOA


curl -i -X GET \
 "https://graph.facebook.com/104343681313462?fields=id,name&access_token=279190169884971|KDCzLdgTS80Sk5FwhQb7WGo3TOA"


 curl -i -X GET "https://graph.facebook.com/100052295641222?fields=birthday,email,hometown&access_token=279190169884971|KDCzLdgTS80Sk5FwhQb7WGo3TOA"