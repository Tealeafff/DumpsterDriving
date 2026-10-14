import csv
from Bio.Blast import NCBIXML

input_xml = "bacterial_blast_results.xml"
output_csv = "candida_hits.csv"

print(f"Parsing {input_xml}...")

with open(input_xml, "r") as result_handle, open(output_csv, "w", newline="") as csv_file:
    blast_record = NCBIXML.read(result_handle)
    
    csv_writer = csv.writer(csv_file)
    
    csv_writer.writerow(["Hit_Number", "Read_ID", "E_Value", "Alignment_Length", "Query_Snippet", "Match_Pattern", "Subject_Snippet"])
    
    hit_count = 0
    
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            hit_count += 1
            
            read_id = alignment.title.split()[1] if len(alignment.title.split()) > 1 else alignment.title
            e_value = hsp.expect
            align_len = hsp.align_length
            
            query_snip = hsp.query[0:50]
            match_snip = hsp.match[0:50]
            sbjct_snip = hsp.sbjct[0:50]
            
            csv_writer.writerow([hit_count, read_id, e_value, align_len, query_snip, match_snip, sbjct_snip])

print(f"Success! {hit_count} environmental variants safely exported to {output_csv}.")