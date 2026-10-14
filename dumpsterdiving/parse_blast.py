from Bio.Blast import NCBIXML

result_handle = open("candida_blast_results.xml")
blast_record = NCBIXML.read(result_handle)

hit_count = 0

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        hit_count += 1
        print(f"**** Alignment {hit_count} ****")
        print(f"Sequence: {alignment.title}")
        print(f"E-value: {hsp.expect}")
        print(hsp.query[0:75] + "...")
        print(hsp.match[0:75] + "...")
        print(hsp.sbjct[0:75] + "...\n")

print(f"Total biological hits found: {hit_count}")
result_handle.close()