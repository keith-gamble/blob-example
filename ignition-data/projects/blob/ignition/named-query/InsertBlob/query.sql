IF NOT EXISTS(SELECT TOP 1 [Blob] from BlobData WHERE [Name] = :name)
	BEGIN
		INSERT INTO BlobData ([Name], [Blob]) VALUES (:name, :blob)
	END
ELSE
	BEGIN
		UPDATE BlobData SET [Blob] = :blob WHERE [Name] = :name
	END