Import-Module ActiveDirectory
$aResults = @()
$List = Get-Content ".\userlist.txt"
ForEach($Item in $List){
	$Item = $Item.Trim()
	#$User = Get-ADUser -Filter{displayName -like $Item -and SamAccountName -notlike "a-*" -and Enabled -eq $True} -Properties SamAccountName, GivenName, Surname, telephoneNumber, mail
	$User = Get-ADUser -Filter{displayName -like $Item} -Properties SamAccountName, GivenName, Surname, mail, EmployeeID
	$hItemDetails = New-Object -TypeName psobject -Property @{
		FullName = $Item
		UserName = $User.SamAccountName
		Email = $User.mail
		EmployeeID = $User.EmployeeID
	}
	#Add data to array
	$aResults += $hItemDetails
}
$aResults | Export-CSV ".\Results.csv"