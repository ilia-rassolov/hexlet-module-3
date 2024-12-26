# BEGIN (write your solution here)
class FakeClient:
    def list_for_users(self, user_name):
        if not user_name:
            return None
        return [{"language": "php" }, {"language": "javascript"}, {"language": "javascript"}, {"language": "python"}]
# END