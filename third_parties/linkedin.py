import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://gist.githubusercontent.com/monisharajan/6da7caa2a835b788596524c0178332c2/raw/af6a2936907f510a14e13b61e20735e40868f734/monisha-rajan.json"

    response = requests.get(api_endpoint)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
