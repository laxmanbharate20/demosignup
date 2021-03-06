# demosignup
1. Register user: 
Postaman: POST http://127.0.0.1:8000/signup/
body ={ "username": "", 
          "first_name": "", 
          "last_name": "", 
          "business_name": "", 
          "business_licn_no": "", 
          "phone_no": , "email": ""
     }

2.  Get JWT token:
postman: POST http://127.0.0.1:8000/get_token/
body= {         username:" "         
                 password:" "
      }
3.  Login 
postman: POST http://127.0.0.1:8000/signin/
body=      {         email:" "         
                    password:" "
            }
