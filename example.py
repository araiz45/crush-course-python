def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for typename, department in group_dictionary.items():
		# Now go through the users in the group
		for dep in department:
			if dep in user_groups:
				user_groups[dep]= typename
			else:
				user_groups[dep] = [typename]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))