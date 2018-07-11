#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<assert.h>
 
#define N 1000000
 
typedef struct node{
	int y;
	int w;
	struct node *next;
}node;
 
node *edges[N];
char visited[N];
unsigned long long time[N];
unsigned long long total_time;
 
void init( ){
	int i;
	total_time = 0;
	for( i = 0; i < N; i++ ) edges[i] = NULL;
	memset( visited, 0, N * sizeof( char ) );
	memset( time, 0, N * sizeof( unsigned long long ) );
}
 
void insert_edge( int x, int y, int w ){
	node *p;
	p = ( node * ) malloc( sizeof( node ) );
	p->y = y;
	p->next = edges[x];
	p->w = w + 2;
	edges[x] = p;
}
 
void print_graph( int n ){
	int i;
	node *p;
 
	for( i = 0; i < n; i++ ){
		p = edges[i];
		printf("vertex %d: ", i );
		while( p ){
			printf("%d(%d)->", p->y, p->w);
			p = p->next;
		}
		printf("NULL\n");
	}
}
 
void delete_graph( int n ){
	int i;
	node *p;
 
	for( i = 0; i < n; i++ ){
		while( edges[i] ){
			p = edges[i];
			edges[i] = p->next;
			free( p );
		}
	}
	init();
}
 
void dfs( int u ){
	node *p;
 
	visited[ u ] = 1;
	p = edges[ u ];
	//printf("started processing vertex %d\n",  u );
	while( p != NULL ){
		//printf("processing_edge %d->%d\n", u, p->y);
		if( !visited[ p->y ] ){
			dfs( p->y );
		}
		//printf("updaitng time %llu, time[u] = %llu\n", p->w + time[p->y], time[u]);
		if( p->w + time[ p->y ] > time[ u ] )
			time[u] = p->w + time[p->y];
		p = p->next;
	}
	if( total_time < time[u] )
		total_time = time[u];
}
		
int main(){
	int r, p;
	int i;
	int x, y, w;
 
	scanf("%d %d", &r, &p);
	init();
	for( i = 0; i < p; i++ ){
		scanf( "%d %d %d", &x, &y, &w );
		insert_edge( x - 1, y - 1, w );
	}
	//print_graph( r );
	for( i = 0; i < r; i++ )
		if( !visited[i] )
			dfs( i );
	//for( i = 0; i < r; i++ ) printf("%lld ", time[i]);
	printf("%llu\n", total_time);
	//print_graph( r );
	delete_graph( r );
	//print_graph( r );
 
	return 0;
}
