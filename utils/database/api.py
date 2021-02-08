import json
import utils.database.mongo_setup as mongo_setup

from utils.database.users import User
from utils.database.domains import Domain


mongo_setup.global_init()


def add_user(user_id: int) -> User:
    user = User()
    user.user_id = user_id

    user.save()

    return user


def find_user(user_id: int) -> User:
    user = User.objects(user_id=user_id).first()
    
    if not user:
        user = add_user(user_id)
    
    return user


def add_domain(user_id: int, domain_name: str, rhash: str) -> Domain:
    user = find_user(user_id=user_id)
    domain = find_domain_query(user_id=user_id, domain_name=domain_name, user=user)
    if domain:
        domain.update(rhash=rhash)
        user.save()
    else:
        domain = Domain()
        domain.name = domain_name
        domain.rhash = rhash
        user.domains.append(domain)
        user.save()

    return domain


def find_domain_query(user_id: int, domain_name: str, user=None):
    if not user:
        user = find_user(user_id=user_id)

    domain_query = user.domains.filter(name=domain_name)

    return domain_query


def find_domain(user_id: int, domain_name: str, user=None) -> Domain:
    if not user:
        user = find_user(user_id=user_id)

    domain = user.domains.filter(name=domain_name).first()

    return domain


# Seems like it isn't needed
def delete_domain():
    return


def get_domain_list(user_id: int):
    user = find_user(user_id)

    domains = user.domains
    domain_list = {}
    for domain in domains:
        domain_json = json.loads(domain.to_json())
        domain_list[domain_json["name"]] = domain_json["rhash"]

    return domain_list


def get_rhash(user_id: int, domain_name: str):
    domain = find_domain(user_id=user_id, domain_name=domain_name)

    if isinstance(domain, Domain):
        domain_dict = json.loads(domain.to_json())
        rhash = domain_dict.get("rhash")
    else:
        rhash = None

    return rhash
