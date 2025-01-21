get_emp(self, id):
q = f"select * from emp where id={id}"
self.curser.execute(q)
user_dict = {}
user_dict["id"], user_