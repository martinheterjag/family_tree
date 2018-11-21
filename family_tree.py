# -*- coding: utf-8 -*-
import json

db = "./json/family.json"
oldest_gen = 100


with open(db) as f:
    database = json.load(f)

generation = 0
family_members = []
generations = []

for family_member in sorted(database, key=lambda x : x['generation'], reverse=False):
    # Check if we should handle a new generation
    if generation != family_member["generation"]:
        # save list of all members of previous generation in a list of generations.
        if family_members:
            generations.append(family_members)
            family_members = []
        # handle next generation
        print "\ngeneration", family_member["generation"] - oldest_gen, ":",

    family_members.append(family_member)
    print family_member["name"] + ",",
    generation = family_member["generation"]

# Don't forget the last generation
if family_members:
    generations.append(family_members)

print "\n"


# Now we have a list of generations and each generation is a list of family members.

for generation in generations:
    print ""
    print "------------------------------------------------------------------------",
    partner_id = 0
    for family_member in sorted(generation ,key=lambda x : x['partner_id'], reverse=False):
        if family_member["partner_id"] == partner_id:
            print "❤", 
        else:
            print "\n", family_member["partner_id"],b
        print family_member["name"], u'vars förälder är', family_member["parent"],
        partner_id = family_member["partner_id"]

print ""
print "------------------------------------------------------------------------"
print ""
print ""