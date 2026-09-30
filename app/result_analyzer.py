ALLOWED_STATUSES = {
			"PASS",
			"FAIL",
			"BLOCKED",
			"SKIPPED"
					}
def validate_results(results):
	if not isinstance(results, list):
		raise TypeError("results needs to be a list")
	for result in results:
		if not isinstance(result, str):
			raise TypeError("result needs to be a string")
		if result not in ALLOWED_STATUSES:
			raise ValueError("Invalid status, must be PASS, FAIL, BLOCKED, or SKIPPED")	

def count_statuses(results):
	counts = {}
	validate_results(results)
	for status in results:
		if status not in counts:
			counts[status] = 1
		else:
			counts[status] += 1
	return counts

def calculate_pass_rate(results):
	validate_results(results)
	pass_rate = 0
	num_of_pass = 0
	total_statuses = len(results)
	if total_statuses == 0:
		return 0.0
	for status in results:
		if status == "PASS":
			num_of_pass += 1
	pass_rate = (num_of_pass) /(total_statuses) * 100
	return round(pass_rate, 2)

def summarize_results(results):
	validate_results(results)
	pass_rate = calculate_pass_rate(results)
	counts = count_statuses(results)
	summary = {
			"total":len(results),
			"counts": counts,
			"pass_rate":pass_rate 
						}
	return summary
