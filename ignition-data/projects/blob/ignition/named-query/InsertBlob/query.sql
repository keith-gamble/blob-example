IF NOT EXISTS(SELECT TOP 1 [Blob] from BlobData WHERE [Name] = :name)
	BEGIN
		INSERT INTO BlobData ([Name], [Blob], [FileType]) VALUES (:name, :blob, :fileType)
	END
ELSE
	BEGIN
		UPDATE BlobData SET [Blob] = :blob, [FileType] = :fileType WHERE [Name] = :name
	END