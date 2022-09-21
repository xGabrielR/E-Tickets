import requests

class PicPayRequest():
    
    def __init__(self, picpay_token, seller_token, url_callback, url_return):
        self.__url = "https://appws.picpay.com/ecommerce/public"
        self.__picpay_token = picpay_token
        self.__seller_token = seller_token
        self.__url_callback = url_callback
        self.__url_return = url_return

    @property
    def _picpay_token(self):
        return self.__picpay_token

    @property
    def _seller_token(self):
        return self.__seller_token

    @property
    def get_picpay_header(self) -> dict:
        header_dict = {
            "x-picpay-token": self._picpay_token,
            "x-seller-token": self._seller_token,
        }

        return header_dict
    
    def get_picpay_request(self, auth_user_checkout: dict) -> dict:
        request_dict = {
            "referenceId": f"{auth_user_checkout['product_id']}",
            "callbackUrl": self.__url_callback,
            "returnUrl": self.__url_return,
            "expiresAt": f"{auth_user_checkout['expires_date']}",
            "value": f"{float(auth_user_checkout['price'])}",
            "buyer": {
                "firstName": f"{auth_user_checkout['first_name']}",
                "lastName": f"{auth_user_checkout['last_name']}",
                "document": f"{auth_user_checkout['cpf']}",
                "email": f"{auth_user_checkout['email']}",
                "phone": f"{auth_user_checkout['phone']}"
            }
        }

        return request_dict

    def make_payment_request(self, request_dict: dict):
        url_path = self.__url + '/payments'

        r = requests.post(
                url=url_path,
                json=request_dict
        )

        # Future Validations

        return r