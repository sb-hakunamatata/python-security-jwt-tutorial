class IUserModel:
    def getUser(self, user_id: str):
        pass


class UserModel(IUserModel):
    def getUser(self, user_id: str):
        return {
            "user": "user_id",
            "company": "random"
        }
