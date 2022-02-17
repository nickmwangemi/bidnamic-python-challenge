import csv
import os


from records.models import AdGroup, Campaign, SearchTerm



csv_dir_path = os.path.dirname(os.path.abspath(__file__))


def run():
    # AdGroup
    file = open(csv_dir_path + "/adgroups.csv")
    records = csv.reader(file, delimiter=",")

    adgroup_instances = []
    for count, record in enumerate(records, start=1):
        if count != 1:
            adgroup_instances.append(
                AdGroup(
                    ad_group_id=record[0],
                    campaign_id=record[1],
                    alias=record[2],
                    status=record[3],
                )
            )
    AdGroup.objects.bulk_create(adgroup_instances)
    print(f"Success! {len(adgroup_instances)} Ad Group instances have been loaded into the database.")

    # Campaign
    file = open(
        csv_dir_path + "/campaigns.csv"
    )
    records = csv.reader(file, delimiter=",")

    campaign_instances = []
    for count, record in enumerate(records, start=1):
        if count != 1:
            campaign_instances.append(
                Campaign(
                    campaign_id=record[0], structure_value=record[1], status=record[2]
                )
            )
    Campaign.objects.bulk_create(campaign_instances)
    print(f"Success! {len(campaign_instances)} Campaign instances have been loaded into the database.")


    # SearchTerm
    file = open(
        csv_dir_path + "/search_terms.csv"
    )
    records = csv.reader(file, delimiter=",")

    search_term_instances = []
    for count, record in enumerate(records, start=1):
        if count != 1:
            search_term_instances.append(
                SearchTerm(
                    date=record[0],
                    ad_group_id=record[1],
                    campaign_id=record[2],
                    clicks=record[3],
                    cost=record[4],
                    conversion_value=record[5],
                    conversions=record[6],
                    search_term=record[7],
                )
            )
    SearchTerm.objects.bulk_create(search_term_instances)
    print(f"Success! {len(search_term_instances)} Search term instances have been loaded into the database.")

