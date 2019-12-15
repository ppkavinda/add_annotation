import glob

def addAnnotation(file):
    importline = 6

    NOTNULL_ANNOT = '@NotNull'
    OPTIONAL_ANNOT = '@Basic(optional = false)'

    CREATED_AT_PHRASE = '\"created_at\"'
    CREATED_IMPORT = 'import org.hibernate.annotations.CreationTimestamp;\n'
    CREATED_TIMESTAMP = '@CreationTimestamp'

    UPDATED_AT_PHRASE = '\"updated_at\"'
    UPDATED_IMPORT = 'import org.hibernate.annotations.UpdateTimestamp;\n'
    UPDATED_TIMESTAMP = '@UpdateTimestamp'

    file.seek(0)
    lines = file.readlines()
    file.seek(0)
    for i, line in enumerate(lines):
        if CREATED_AT_PHRASE in line:
            if CREATED_TIMESTAMP not in lines[i-1]:
                if NOTNULL_ANNOT in lines[i-2] or OPTIONAL_ANNOT in lines[i-2]:
                    lines[i-2] = ""
                if NOTNULL_ANNOT in lines[i-1] or OPTIONAL_ANNOT in lines[i-1]:
                    lines[i-1] = "    " + CREATED_TIMESTAMP + "\n"
                else:
                    lines[i] = "    " + CREATED_TIMESTAMP + "\n" + lines[i]
                    
                lines[importline] = lines[importline] + CREATED_IMPORT
                
            elif CREATED_TIMESTAMP in lines[i-1]:
                if NOTNULL_ANNOT in lines[i-2] or OPTIONAL_ANNOT in lines[i-2]:
                    lines[i-2] = ""
                if NOTNULL_ANNOT in lines[i-3] or OPTIONAL_ANNOT in lines[i-3]:
                    lines[i-3] = ""

                
        if UPDATED_AT_PHRASE in line:
            if UPDATED_TIMESTAMP not in lines[i-1]:
                if NOTNULL_ANNOT in lines[i-2] or OPTIONAL_ANNOT in lines[i-2]:
                    lines[i-2] = ""
                if NOTNULL_ANNOT in lines[i-1] or OPTIONAL_ANNOT in lines[i-1]:
                    lines[i-1] = "    " + UPDATED_TIMESTAMP + "\n"
                else:
                    lines[i] = "    " + UPDATED_TIMESTAMP + "\n" + lines[i]
                
                lines[importline] = lines[importline] + UPDATED_IMPORT
                
            elif UPDATED_TIMESTAMP in lines[i-1]:
                if NOTNULL_ANNOT in lines[i-2] or OPTIONAL_ANNOT in lines[i-2]:
                    lines[i-2] = ""
                if NOTNULL_ANNOT in lines[i-3] or OPTIONAL_ANNOT in lines[i-3]:
                    lines[i-3] = ""
                    
    file.seek(0)
    file.writelines(lines)
    print("completed : " + file.name)

    
entities = glob.glob('*.java')
for entity in entities:
    with open (entity, 'r+') as file:
        addAnnotation(file)

print("finish. bye:)")


