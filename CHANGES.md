v1.1.0
- Show more fields on plasmid table and same fields for principal tables
- Make unique together for plasmid: name, reference, supplier, lab
- Show more fields on enzyme table
- Make unique together for enzyme: name, reference, supplier, lab
- Show more fields on primer table
- Make unique together for primer: name, sequence, lab, supplier
- Show more fields on antibody table
- Make unique together for antibody: name, reference, supplier, lab
- Max length for antibody name and reactivity is now 100 characters
- Show more fields on chemicals table
- Make unique together for chemicals: name, reference, supplier, lab
- Max length for chemical name is now 100 characters
- Adds new field on antibody: stock concentration
- Changes name of antibody field Primary/Secondary para Primary/Secondary/Tracer
- Adds lab to antibody
- Fixes search problem. Removed unnecessary IDs
- Excel data imported to database
