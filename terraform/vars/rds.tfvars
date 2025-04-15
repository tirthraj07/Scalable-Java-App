# Network Vars
region              = "us-east-1"
vpc_id              = "vpc-08a472602d8aaf06f"
subnet_ids          = ["subnet-08e7c89184c3f0959", "subnet-0a8786ff7cc1b5b9e", "subnet-0d3461852f9ae03e9"]
multi_az            = false
publicly_accessible = true

# DB Vars
db_engine                   = "mysql"
db_storage_type             = "gp2"
db_username                 = "root"
db_instance_class           = "db.t3.micro"
db_storage_size             = 20
set_secret_manager_password = true
set_db_password             = false
db_password                 = "tirthraj07"

# Security Group Vars
ingress_from_port   = 3306
ingress_to_port     = 3306
ingress_protocol    = "tcp"
ingress_cidr_blocks = ["0.0.0.0/0"]

egress_from_port   = 0
egress_to_port     = 0
egress_protocol    = "-1"
egress_cidr_blocks = ["0.0.0.0/0"]

# Backup vars
backup_retention_period  = 7
delete_automated_backups = true
copy_tags_to_snapshot    = true
skip_final_snapshot      = true
apply_immediately        = true

# Parameter store
parameter_store_secret_name = "/dev/petclinic/rds_endpoint"
type                        = "String"

# Tag Vars
owner       = "root"
environment = "dev"
cost_center = "techiescamp-commerce"
application = "rds"