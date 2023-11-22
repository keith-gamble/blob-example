def doGet(request, session):
	name = request['remainingPath'][1:]
	system.util.getLogger("Blob").info("Querying for ... %s" % name)
	blob_data = system.db.runNamedQuery(system.util.getProjectName(), "GetBlob", {"name": name})
	return {"html": str(blob_data)}