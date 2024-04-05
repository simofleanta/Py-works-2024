select
c.sustcompanyid as "company id",
c.companynamesus,
c.ch,
c.rr,
c.cg,
c.crrcg, 
rrp.lastupdate as "update",
rrp.jobid,
a.researchtypeid,
rrp.unmanagedrisk as "ESG Risk Rating",
rrp.management as "management score",
rrp.exposure as "company exposure",
rrp.manageablerisk as "manageable risk",
rrp.unmanageablerisk as "unmanageable risk",
'Comprehensive' as "Core/Comprehensive",
rrp.major,
rrp.minor,
rrp.patch,
rrp.managedrisk,
rrm.meicode as meicode,
'RR_MEI_and_idios' as "frommei",
rrm.management as "issue management",
rrm.unmanagedrisk as "Issue Unmanaged Risk Score",
rrm.exposure as "Issue exposure score",
rrm.subindustryexposurescore as "Issue Default Exposure Sore",
rrm.finalbetafactor as "Issue Beta",
rrm.issuemanagementweight as "Issue Unmanaged Risk Contribution",
rrp.manageableriskfactor as "Manageable Risk Factor",
rrm.finalweight * 100.00 as "Contribution to ESG Risk Rating",
rri.answercategory,
rrm.manageablerisk as "issue manageable risk",
rrm.manageableriskfactor as "issue manageable risk factor",
rrm.managedrisk as "issue managed risk",
rrm.unmanageablerisk as "issue unmanageable risk",
rrt.description,
rrt.id
from profiles_historical.rrpublishedprofiles rrp
join profiles_historical.rrmaterialesgissues rrm on rrp.publishedprofileid = rrm.publishedprofileid
left join profiles_historical.rrindicators rri on rri.materialesgissueid = rrm.materialesgissueid and rrm.meicode like 'EV.%'
join cddb.corporatedata c on rrp.companyid = coalesce(c.researchentityid, c.sustcompanyid)
join jobs.archive a on a.id = rrp.jobid
join jobs.researchtypes rrt on rrt.id = a.researchtypeid 
--where rrp.publishedprofileid = -999997944
union all 
select
c.sustcompanyid as "company id",
c.companynamesus, 
c.ch,
c.rr,
c.cg, 
c.crrcg, 
crrp.lastupdate as "update",
crrp.jobid,
a.researchtypeid,
crrp.unmanagedrisk as "ESG Risk Rating",
crrp.management as "management score",
crrp.exposure as "company exposure", 
crrp.manageablerisk as "manageable risk",
crrp.unmanageablerisk as "unmanageable risk",
'Core' as "Core/Comprehensive",
crrp.major,
crrp.minor,
crrp.patch,
crrp.managedrisk,
crri.code as meicode,
'CRR_events' as "frommei",
null as "issue management",
null as "Issue Unmanaged Risk Score",
null as "Issue exposure score",
null as "Issue Default Exposure Sore",
null as "Issue Beta",
null as "Issue Unmanaged Risk Contribution",
null as "Manageable Risk Factor",
null as "Contribution to ESG Risk Rating",
null as answercategory,
null as "issue manageable risk",
null as "issue manageable risk factor",
null as "issue managed risk",
null as "issue unmanageable risk",
rrt.description,
rrt.id
from profiles_historical.crrpublishedprofiles crrp
join profiles_historical.crrindicators crri on crrp.publishedprofileid = crri.publishedprofileid and crri.code like 'EV.%'
join cddb.corporatedata c on crrp.companyid = coalesce(c.researchentityid, c.sustcompanyid)
join jobs.archive a on a.id = crrp.jobid
join jobs.researchtypes rrt on rrt.id = a.researchtypeid



select * from jobs.archive a 





