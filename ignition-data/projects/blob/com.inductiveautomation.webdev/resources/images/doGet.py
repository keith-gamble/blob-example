def doGet(request, session):
	name = request['remainingPath'][1:]
	system.util.getLogger("Blob").info("Querying for ... %s" % name)
	ds = system.db.runNamedQuery(system.util.getProjectName(), "GetBlob", {"name": name})
	
	if ds.getRowCount() == 0:
		system.util.getLogger("Blob").info("No rows for: %s" % name)
		return {"html": ""}
	
	blob_data = ds.getValueAt(0, 0)
	mime_type = ds.getValueAt(0, 1)
	
	system.util.getLogger("Blob").info("%s is a: %s" % (name, file_type))
	return {"bytes": blob_data, "contentType": mime_type}